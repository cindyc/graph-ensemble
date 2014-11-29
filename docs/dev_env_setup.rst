Setting up MongoDB: 
==================
brew update
brew install mongodb
pip install pymongo



Setting Up Bulbs, Neo4j and Gremlin
===================================
1. Download the Community Edition Neo4J from neo4j.com/download

2. Install Neo4j: 
   http://neo4j.com/docs/stable/server-installation.html
   it will be installed under /usr/local/Cellar/neo4j/2.1.4/libexec

3. Start Neo4j server: 
   /usr/local/neo4j/bin/neo4j start
   Using additional JVM arguments:  -server -XX:+DisableExplicitGC -Dorg.neo4j.server.properties=conf/neo4j-server.properties -Djava.util.logging.config.file=conf/logging.properties -Dlog4j.configuration=file:conf/log4j.properties -XX:+UseConcMarkSweepGC -XX:+CMSClassUnloadingEnabled
   Starting Neo4j Server...WARNING: not changing user
   process [18440]... waiting for server to be ready..... OK.
   http://localhost:7474/ is ready.

Installing Gremlin (Gremlin is a domain-specific-language for graph databases)
git clone https://github.com/tinkerpop/gremlin.git
cd gremlin
mvn clean install

Gremlin plugin is no longer bundled with Neo4j, to install the plugin: 
http://stackoverflow.com/questions/21637155/no-such-serverplugin-gremlinplugin
https://github.com/thinkaurelius/neo4j-gremlin-plugin

Set JAVA_HOME to work around the following problem: 
http://www.jayway.com/2013/03/08/configuring-maven-to-use-java-7-on-mac-os-x/
http://stackoverflow.com/questions/17824889/how-to-force-maven-3-1-to-use-right-version-of-java-on-mac-os-8-10

echo JAVA_HOME=/usr/libexec/java_home -v 1.8*` | sudo tee -a /etc/mavenrc`
if the above doesn't work, do the following: 
export JAVA_HOME="/Library/Java/JavaVirtualMachines/jdk1.7.0_67.jdk/Contents/Home"
sudo echo JAVA_HOME="/Library/Java/JavaVirtualMachines/jdk1.7.0_67.jdk/Contents/Home" > /etc/mavenrc

git clone https://github.com/neo4j-contrib/gremlin-plugin.git
mvn clean package
unzip target/neo4j-gremlin-plugin-*-server-plugin.zip -d $NEO4J_HOME/plugins/gremlin-plugin

Add the following line to $NEO4J_HOME/conf/neo4j-server.properties
org.neo4j.server.thirdparty_jaxrs_classes=com.thinkaurelius.neo4j.plugins=/tp

cd $NEO4J_HOME
bin/neo4j restart

Install bulbs from my repo, it has the gremlin.groovy listed below fix:
pip install -e git://github.com/cindyc/bulbs.git@master#egg=bulbs


"ValueError: ({... "message": "groovy.lang.MissingMethodException: No signature of method: groovy.lang.MethodException.setMaxBufferSize() is applicable for argument types: ()" })
"ValueError: ({... "message": "groovy.lang.MissingMethodException: No signature of method: groovy.lang.MethodException.StartTransaction() is applicable for argument types: ()" })

Or fix the errors manually: 


In [8]: g.scripts.source_file_map
Out[8]: OrderedDict([('/Users/cindy.cao/.virtualenvs/modelgenie/lib/python2.7/site-packages/bulbs/gremlin.groovy', 'gremlin'), ('/Users/cindy.cao/.virtualenvs/modelgenie/lib/python2.7/site-packages/bulbs/neo4jserver/gremlin.groovy', 'gremlin')])

Open /Users/cindy.cao/.virtualenvs/modelgenie/lib/python2.7/site-packages/bulbs/gremlin.groovy 
Delete or comment these 2 methods everywhere: 
  //g.setMaxBufferSize(0)
    //g.startTransaction()

https://groups.google.com/forum/#!msg/gremlin-users/10ppC5b7g6w/xmMpTU5BLggJ
