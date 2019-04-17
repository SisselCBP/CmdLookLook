#!/usr/bin/env python
# coding: utf-8
# @Author: Sissel
# @Date: 2019-03-10 11:59:32
# 这只竹鼠很漂亮呀

import os
import nmap

from settings import *
from log import *
from load_script import *

# 构造包
from scapy.all import srp, Ether, ARP
class PortScanner():
    def __init__(self):
        pass
    
    def start(self, ip):
        nm = nmap.PortScanner()
        log.info('scanning start, ip {}'.format(ip))
        nm.scan(ip, arguments='')
        # 列出结果
        for host in nm.all_hosts():
            log.info('Host : %s (%s)' % (host, nm[host].hostname()))
            log.info('State : %s' % nm[host].state())
            for proto in nm[host].all_protocols():
                log.info('Protocol : %s' % proto)
                lport = nm[host][proto].keys()
                lport.sort()
                for port in lport:
                    log.info('port : %s\tstate : %s' % (port, nm[host][proto][port]['state']))

class HostScanner():
    def __init__(self):
        log.debug('Init an Host Scanner')
        pass
    
    def start(self, IpScan='192.168.31.1/24'):
        return self.arp_scan(IpScan)
        
    def arp_scan(self, IpScan='192.168.31.1/24'):
        #IpScan = '192.168.114.1/24'
        log.info('Host Scan Start: {}'.format(IpScan))
        ip_list = []
        try:
            ans,unans = srp(Ether(dst="FF:FF:FF:FF:FF:FF")/ARP(pdst=IpScan), timeout=2)
        except Exception as e:
            log.error(e)
        else:
            for send, rcv in ans:
                MAC_address = rcv.sprintf("%Ether.src%")
                ip_address = rcv.sprintf("%ARP.psrc%")
                log.info(ip_address)
                ip_list.append(ip_address)
        log.debug(ip_address)
        return ip_list
       
if __name__ == "__main__":
    p_scanner = PortScanner()
    p_scanner.start('127.0.0.1')
