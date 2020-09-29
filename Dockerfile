FROM node:latest
LABEL version=1.1.0


#EXPOSE 19000
#EXPOSE 19001

#ENV ADB_IP="192.168.1.105"
#ENV REACT_NATIVE_PACKAGER_HOSTNAME="192.168.1.123"

# Create and define the working directory
RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app/

# Install the application's dependencies
COPY package.json /usr/src/app/
COPY package-lock.json /usr/src/app/
RUN npm install

# Copy contents of application into working directory and install expo-cli globally
COPY . /usr/src/app/
RUN npm install -g expo-cli 

# ENTRYPOINT [ "/usr/local/bin/npm", "start"]
# ENTRYPOINT [ "/bin/bash" ]

