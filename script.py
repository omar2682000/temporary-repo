# Configure tomcat port
server_config = open("/var/lib/tomcat9/conf/server.xml", "rt")
text = server_config.readlines()
for index in range(len(text)):
    text[index] = text[index].replace("8080", "8090")
server_config.close()

server_config = open("/var/lib/tomcat9/conf/server.xml", "wt")
server_config.writelines(text)
server_config.close()


# Configure tomcat users
users_conf = """
<role rolename="manager-gui"/>
<role rolename="manager-script"/>
<user username="admin" password="admin" roles="manager-gui,manager-script"/>
"""
tomcat_users = open("/var/lib/tomcat9/conf/tomcat-users.xml", "rt")
text = tomcat_users.readlines()
text.insert(max(0, len(text) - 1), text)
tomcat_users.close()

tomcat_users = open("/var/lib/tomcat9/conf/tomcat-users.xml", "wt")
tomcat_users.writelines(text)
tomcat_users.close()
