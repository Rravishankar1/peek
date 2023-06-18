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
//   const { loading: loadingDiscord, error: errorDiscord, data: dataDiscord} = useQuery(CONTINENT_QUERY, {
//     variables: {
//       request: {
//         userID: 21,
//         appID: "DISCORD",
//       },
//     },
//   });
//   //   console.log(data.getNew, loading, error);

//   const { loading: loadingGmail, error: errorGmail, data: dataGmail} = useQuery(CONTINENT_QUERY, {
//     variables: {
//       request: {
//         userID: 21,
//         appID: "GMAIL",
//         token1: "ya29.a0AWY7CkkhT2XECVu6GmqVCoxJPTnlxsO8zshE9Fb4IbGs74lnkOff54XZA4D_RApOUhzSfuvsCe4KKNsGq9aaE4-RsD9S01aft959tgzo5dj-SqPJNy3WN6uV_EZVyWwn-TMAu_5PD8S_F2gCOnEiLAydBAtpaCgYKAYMSARESFQG1tDrpAmiELvLYAKVyk9PLbQm8-g0163",// access token,
//         token2: "1//04afQet5bTZPbCgYIARAAGAQSNwF-L9Ird1dyGLcgnSAs6A4MR7H-3PzuP8_zhMsPWROp2m6Rzyx-YVlzd-1IQ6CilTy-BlE6wMU", // refresh token,
//         token3: "569421655023-8rrv1eve2nmee1ajes87tskpkl69mb6l.apps.googleusercontent.com", // client key
//         token4: "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", //client secret
//       },
//     },
//   });
//   if (loadingDiscord || loadingGmail) return <Text>Loading</Text>;

  return (
    <SafeAreaView style={styles.container}>
      {/* <View style={styles.titleContainer}>
        <Text style={styles.title}>Peek Into</Text>
      </View>
      <ScrollView>
      <View style={styles.appContainer}>
       <AppContainer topics={discordResponse} app={"gmail"}></AppContainer>
      </View>
      <View style={styles.appContainer}>
      <AppContainer topics={discordResponse} app={"discord"}></AppContainer> 
      </View>
      </ScrollView> */}
      <LoginContainer/>
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
    backgroundColor: "#000",
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
