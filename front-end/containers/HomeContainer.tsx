import React, { useState } from "react";
import {
  StyleProp,
  View,
  StyleSheet,
  Text,
  Image,
  ScrollView,
  TouchableOpacity,
  SafeAreaView,
} from "react-native";
import { themes, GUTTER } from "../theme/styles/Themes";
import { useQuery } from "@apollo/client";
import { CONTINENT_QUERY } from "../gql/Query";
import AppContainer from "./AppContainer";
import LoginContainer from "./LoginContainer";

const HomeContainer: React.FC = () => {
  const {
    loading: loadingDiscord,
    error: errorDiscord,
    data: dataDiscord,
  } = useQuery(CONTINENT_QUERY, {
    variables: {
      request: {
        userID: 123,
        appID: "DISCORD",
      },
    },
  });
  //   console.log(data.getNew, loading, error);
  const {
    loading: loadingReddit,
    error: errorReddit,
    data: dataReddit,
  } = useQuery(CONTINENT_QUERY, {
    variables: {
      request: {
        userID: 123,
        appID: "REDDIT",
      },
    },
  });

  const {
    loading: loadingGmail,
    error: errorGmail,
    data: dataGmail,
  } = useQuery(CONTINENT_QUERY, {
    variables: {
      request: {
        userID: 123,
        appID: "GMAIL",
      },
    },
  });
  if (loadingDiscord || loadingReddit || loadingGmail)
    return <Text>Loading</Text>;
  const discordResponse = dataDiscord.getCachedData
    ? dataDiscord.getCachedData.topics
    : dataDiscord.getNewData.topics;
  const redditResponse = dataReddit.getCachedData
    ? dataReddit.getCachedData.topics
    : dataReddit.getNewData.topics;
  const gmailResponse = dataGmail.getCachedData
    ? dataGmail.getCachedData.topics
    : dataGmail.getNewData.topics;

  console.log(discordResponse);

  return (
    <SafeAreaView style={styles.container}>
      <View style={styles.titleContainer}>
        <Text style={styles.title}>Peek Into</Text>
      </View>
      <ScrollView>
        <View style={styles.appContainer}>
          <AppContainer topics={discordResponse} app={"discord"}></AppContainer>
        </View>
        <View style={styles.appContainer}>
          <AppContainer topics={redditResponse} app={"reddit"}></AppContainer>
        </View>
        <View style={styles.appContainer}>
          <AppContainer topics={gmailResponse} app={"gmail"}></AppContainer>
        </View>
      </ScrollView>
      {/* <LoginContainer/> */}
    </SafeAreaView>
    // <Text>hello</Text>
  );
};

const styles = StyleSheet.create({
  appContainer: {
    margin: GUTTER * 2,
  },
  container: {
    flex: 1,
    backgroundColor: "#1D1F1D",
    height: "100%",
  },
  titleContainer: {
    marginVertical: GUTTER * 2,
    alignItems: "center",
  },
  title: {
    fontSize: 32,
    color: "#fff",
  },
});

export default HomeContainer;

