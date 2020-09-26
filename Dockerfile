FROM node:latest
LABEL version=1.1.0


#EXPOSE 19000
#EXPOSE 19001

#ENV ADB_IP="192.168.1.105"
#ENV REACT_NATIVE_PACKAGER_HOSTNAME="192.168.1.123"

RUN apt-get update && npm install -g expo-cli \
@react-native-community/hooks@^2.6.0 \
&& yarn add expo

# WORKDIR /fishing_app
COPY . .

ENTRYPOINT [ "/usr/local/bin/npm", "start"]
# ENTRYPOINT [ "/bin/bash" ]

