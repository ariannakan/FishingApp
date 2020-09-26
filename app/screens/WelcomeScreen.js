import React from "react";
import {
  ImageBackground,
  StyleSheet,
  View,
  Image,
  Text,
  Platform,
} from "react-native";

function WelcomeScreen(props) {
  return (
    <ImageBackground
      style={styles.background}
      source={require("../assets/cool-background.png")}
    >
      <View style={styles.logoContainer}>
        <Image style={styles.logo} source={require("../assets/fishing.png")} />
        <Text style={{ fontSize: 30, color: "darkcyan" }}>
          Where's the fish?
        </Text>
      </View>
      <View style={styles.loginButton}></View>
    </ImageBackground>
  );
}

const styles = StyleSheet.create({
  background: {
    flex: 1,
    justifyContent: "flex-end",
    alignItems: "center",
  },
  logo: {
    width: 200,
    height: 200,
    bottom: 20,
  },
  logoContainer: {
    position: "absolute",
    alignItems: "center",
    top: 200,
  },
  loginButton: {
    width: "100%",
    height: 70,
    backgroundColor: "#0F3B5F",
  },
});

export default WelcomeScreen;
