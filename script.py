server_config = open("/usr/share/tomcat9/conf/server.xml", "rt")
text = server_config.readlines()
for index in range(len(text)):
    text[index] = text[index].replace("8080", "8090")
server_config.close()

server_config = open("/var/lib/tomcat7/conf/server.xml", "wt")
server_config.writelines(text)
server_config.close()
