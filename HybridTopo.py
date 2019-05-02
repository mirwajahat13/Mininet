#usr/bin/python

Topology of 6 nodes and 6 switches. The switches s4 and s5 are legacy switches with no connection to the controller as described in the code 
from mininet.node import RemoteController
from mininet.net import *
from mininet.cli import CLI
from mininet.log import *
from mininet.link import *

def Hybridtopology():
    net = Mininet( topo=None,listenPort=6633,build=False,ipBase='10.0.0.0/8')
    info( '*** Adding controller\n' )
    c1 = net.addController("c1",controller=RemoteController,ipBase="127.0.0.0")
    info( '*** Add switches\n')
    s1 = net.addSwitch('s1', cls=OVSKernelSwitch, failMode='secure')
    s2 = net.addSwitch('s2', cls=OVSKernelSwitch, failMode='secure')
    s3 = net.addSwitch('s3', cls=OVSKernelSwitch, failMode='secure')
    s4 = net.addSwitch('s4', cls=OVSKernelSwitch, failMode='standalone')
    s5 = net.addSwitch('s5', cls=OVSKernelSwitch, failMode='standalone')
    s6 = net.addSwitch('s6', cls=OVSKernelSwitch, failMode='secure')

    info( '*** Add hosts\n')
    h1 = net.addHost('h1', cls=Host, ip='10.0.0.1')
    h2 = net.addHost('h2', cls=Host, ip='10.0.0.2')
    h3 = net.addHost('h3', cls=Host, ip='10.0.0.3')
    h4 = net.addHost('h4', cls=Host, ip='10.0.0.4')
    h5 = net.addHost('h5', cls=Host, ip='10.0.0.5')
    h6 = net.addHost('h6', cls=Host, ip='10.0.0.6')

    info( '*** Add links\n')
    net.addLink(h1, s1)
    net.addLink(h2, s2)
    net.addLink(h3, s3)
    net.addLink(h4, s4)
    net.addLink(h5, s5)
    net.addLink(h6, s6)
    net.addLink(s1, s2)
    net.addLink(s2, s3)
    net.addLink(s3, s4)
    net.addLink(s4, s5)
    net.addLink(s5, s6)
    
    for switch in net.switches:
      for intfs in switch.intfList():
         info( intfs, ': ', switch.ports[intfs], '\n')
     
     

    info( '*** Starting network\n')
    net.build()
    info( '*** Starting controllers\n')
    for controller in net.controllers:
        controller.start()
    
    for switch in net.switches:
     if (switch.failMode=="standalone"):
       info( switch.name + ' ')
       switch.start( [ ] )
     else :
       info( switch.name + ' ')
       switch.start( net.controllers )
   
    info( '*** Topology Running\n')

    CLI(net)
    net.stop()

if __name__ == '__main__':
    setLogLevel( 'info' )
    Hybridtopology()
                   
                   
                   
