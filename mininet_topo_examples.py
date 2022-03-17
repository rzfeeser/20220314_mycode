#!/usr/bin/python3
"""Alta3 Research | Custom topology example

   # assumes this script is named 
   sudo mn --custom mininet_topo_examples.py --topo mytopo # build MyTopo
   sudo mn --custom mininet_topo_examples.py --topo myzopo # build MyZopo 
   """

from mininet.topo import Topo

class MyTopo( Topo ):
       "Simple topology example."

       def __init__( self ):
           "Create custom topo."

           # Initialize topology
           Topo.__init__( self )

           # Add hosts and switches
           leftHost = self.addHost( 'h1' )  # create the obj leftHost and give it the visable name h1
           rightHost = self.addHost( 'h2' )
           leftSwitch = self.addSwitch( 's3' ) # create the obj leftSwitch and give it the visable name s3
           rightSwitch = self.addSwitch( 's4' )

           # Add links
           self.addLink( leftHost, leftSwitch )
           self.addLink( leftSwitch, rightSwitch )
           self.addLink( rightSwitch, rightHost )


class MyZopo( Topo ):
       "Another topology example."

       def __init__( self ):
           "Create custom topo."

           # Initialize topology
           Topo.__init__( self )

           # Add hosts and switches
           leftHost = self.addHost( 'h1' )  # create the obj leftHost and give it the visable name h1
           rightHost = self.addHost( 'h2' )
           centerHost = self.addHost( 'h3' )
           centerSwitch = self.addSwitch( 's1' ) # create the obj leftSwitch and give it the visable name s3

           # Add links
           self.addLink( leftHost, centerSwitch )
           self.addLink( rightHost, centerSwitch )
           self.addLink( centerHost, centerSwitch )




topos = {'mytopo': (lambda: MyTopo()), 'myzopo': (lambda: MyZopo())}
