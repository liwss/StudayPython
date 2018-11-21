# -*- coding: utf-8 -*-

# @Author   : lws
# @Time     : 2018/11/21 14:36
# @describe : 分布式锁的API封装


import logging, os, time
from kazoo.client import KazooClient
from kazoo.client import KazooState
from kazoo.recipe.lock import Lock

logging.basicConfig()


class ZooKeeperLock():
    def __init__(self, hosts, lock_path, lock_name, lock_value, timeout=1):
        self.hosts = hosts
        self.zk_client = None
        self.timeout = timeout
        self.name = lock_name
        self.lock_path = "PolicyCtrlCent/" + lock_path + "/" + lock_name
        self.lock_value = lock_value
        self.lock_handle = None

        self.create_lock()

    def create_lock(self):
        try:
            self.zk_client = KazooClient(hosts=self.hosts, timeout=self.timeout)

            @self.zk_client.add_listener
            def my_listener(state):
                if state == KazooState.LOST:
                    print("LOST")
                elif state == KazooState.SUSPENDED:
                    print("SUSPENDED")
                else:
                    print("Connected")

            self.zk_client.start(timeout=self.timeout)
            self.add_zk_auth()

        except Exception, ex:
            self.init_ret = False
            self.err_str = "Create KazooClient failed! Exception: %s" % str(ex)

        try:
            print self.lock_path
            self.lock_handle = Lock(self.zk_client, self.lock_path)
            self.zk_client.set(self.lock_path, self.lock_value)
        except Exception, ex:
            self.init_ret = False
            self.err_str = "Create lock failed! Exception: %s" % str(ex)

        from kazoo.security import make_digest_acl
        client = self.zk_client
        acl = make_digest_acl('pcm', 'pcm', all=True)
        try:
            client.set_acls(self.lock_path, [acl])
        finally:
            print("set KazooClient acl SUCCESS!")

    def destroy_lock(self):
        # self.release()

        if self.zk_client != None:
            self.zk_client.stop()
            self.zk_client = None

    def acquire(self, blocking=True, timeout=None):
        if self.lock_handle == None:
            return None

        try:
            return self.lock_handle.acquire(blocking=blocking, timeout=timeout)
        except Exception, ex:
            self.err_str = "Acquire lock failed! Exception: %s" % str(ex)
            return None

    def release(self):
        if self.lock_handle == None:
            return None
        return self.lock_handle.release()

    def __del__(self):
        self.destroy_lock()

    def _makeAuth(self, *args, **kwargs):
        from kazoo.security import make_digest_acl
        return make_digest_acl(*args, **kwargs)

    def add_zk_auth(self):
        username = "pcm"
        password = "pcm"
        digest_auth = "%s:%s" % (username, password)
        acl = self._makeAuth(username, password, all=True)
        self.zk_client.add_auth("digest", digest_auth)
        self.zk_client.default_acl = (acl,)
        print("add zk_auth SUCCESS!")


def main():
    zookeeper_hosts = "127.0.0.1:2181"
    lock_name = "test"
    pid = str(os.getpid())
    lock = ZooKeeperLock(zookeeper_hosts, "asdqe", lock_name, pid)
    print "a"

    ret = lock.acquire(timeout=3)
    print ret
    print "b"
    if not ret:
        return

    for i in range(1, 10):
        time.sleep(1)
        print i
    lock.release()


if __name__ == "__main__":
    try:
        while True:
            main()
            time.sleep(1)
    except Exception, ex:
        print "Ocurred Exception: %s" % str(ex)
        quit()