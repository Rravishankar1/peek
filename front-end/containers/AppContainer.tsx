import React, { useState } from "react";
import {
  StyleProp,
  View,
  StyleSheet,
  Text,
  Image,
  ScrollView,
  TouchableOpacity,
  Animated,
} from "react-native";
import { useNavigation } from "@react-navigation/native";
import { themes, GUTTER } from "../theme/styles/Themes";
import { topic } from "../protos/peek";
import Topic from "../components/Topic";
import ExpandedTopic from "../components/ExpandedTopic";
import { isPropertySignature } from "typescript";
import { useQuery } from "@apollo/client";
import { CONTINENT_QUERY } from "../gql/Query";

interface Props {
  topics: topic[];
  app: string;
}

const app = (app_name: string) => {
  switch (app_name) {
    case "gmail":
      return "../assets/social_icons/gmail.png";
    default: 
        return "../assets/social_icons/gmail.png";
  }
};

const appColor = (app_name: string) => {
    switch (app_name) {
        case "gmail":
            return [themes.gmail_light, themes.gmail_dark];
        case "discord": 
            return [themes.discord_light, themes.discord_dark];
    }
}


const AppContainer: React.FC<Props> = (props) => {
    const [light, dark] = appColor(props.app);
    const expandedStyles = StyleSheet.create({
        container: {
          flex: 0,
        },
        title: {
          fontSize: 20,
          color: "#fff",
        },
        titleContainer: {
          paddingVertical: GUTTER * 2,
        },
        titleLogoContainer: {
          flexDirection: "row",
          alignItems: "center",
          justifyContent: "space-between",
          paddingHorizontal: GUTTER * 3,
        },
        topicContainer: {
          backgroundColor: "transparent",
        },
        width33: {
          width: "33%",
          alignItems: "center",
        },
      });
      
      const styles = StyleSheet.create({
        container: {
          backgroundColor: dark,
          borderRadius: 25,
        //   flex: 1,
          // paddingVertical: GUTTER
        },
        containerExpanded: {
          backgroundColor: "black",
          borderRadius: 25,
          // flex: 1,
        },
        footerLeft: {
          width: "20%",
        },
        footerMiddle: {
          width: "60%",
          alignItems: "center",
          justifyContent: "center",
        },
        footerRight: {
          width: "20%",
        },
        titleContainer: {
          backgroundColor: light,
          borderRadius: 15,
          marginHorizontal: GUTTER * 2,
          paddingHorizontal: GUTTER * 2,
          paddingVertical: GUTTER,
        },
        titleLogoContainer: {
          flexDirection: "row",
          alignItems: "center",
          justifyContent: "center",
          marginVertical: GUTTER * 2,
        },
        title: {
          fontSize: 24,
          color: "#fff",
        },
        topicContainer: {
          backgroundColor: light,
          marginHorizontal: GUTTER * 2,
          borderRadius: 15,
        },
        flexOne: {
          flexGrow: 1,
        },
        footerContainer: {
          marginVertical: GUTTER,
          alignItems: "center",
        },
        footerTextContainer: {
          marginVertical: GUTTER,
        },
        notificationsNumberContainer: {
          justifyContent: "center",
          alignItems: "center",
          borderRadius: 20,
          backgroundColor: light,
          height: 30,
          width: 30,
        },
      });
  const img = require("../assets/social_icons/gmail.png");
  const totalNotifs = props.topics.reduce(
    (accumulator, currentValue) => accumulator + currentValue.notifs.length,
    0
  );
  const [expanded, setExpanded] = useState(false);
  const handlePress = () => {
    setExpanded(!expanded);
  };
  return (
    <View style={styles.flexOne}>
      {expanded === true ? (
        <View style={styles.container}>
          <TouchableOpacity onPress={handlePress}>
            {/* // <View style={styles.container}> */}
            <View style={styles.titleLogoContainer}>
              <Image source={img} />
            </View>
          </TouchableOpacity>
          <ScrollView style={styles.topicContainer}>
            {props.topics.map((topic, topicIndex) => (
              <Topic topic={topic} expanded={expanded} app={props.app}/>
            ))}
          </ScrollView>
          <View style={styles.footerContainer}>
            <View style={styles.notificationsNumberContainer}>
              <Text style={{ color: "white", fontSize: 20 }}>
                {totalNotifs}
              </Text>
            </View>
            <View style={styles.footerTextContainer}>
              <View style={styles.footerLeft}></View>
              <View style={styles.footerMiddle}>
                <Text
                  style={{
                    color: "white",
                    fontSize: 20,
                    textAlign: "center",
                  }}
                >
                  Notifcations Received Since Last Opened
                </Text>
              </View>
              <View style={styles.footerRight}></View>
            </View>
          </View>
        </View>
      ) : (
        <View style={[styles.container, expandedStyles.container]}>
          <View style={expandedStyles.titleLogoContainer}>
            <View style={expandedStyles.width33}>
              <View style={styles.notificationsNumberContainer}>
                <Text style={{ color: "white", fontSize: 20 }}>
                  {totalNotifs}
                </Text>
              </View>
            </View>
            <View style={expandedStyles.width33}>
              <Image source={img} />
            </View>
            <View style={expandedStyles.width33}>
              <View style={expandedStyles.titleContainer}>
                <Text style={expandedStyles.title}>
                  {props.topics.length} Peeks
                </Text>
              </View>
            </View>
          </View>
          <ScrollView
            style={[styles.topicContainer, expandedStyles.topicContainer]}
          >
            {props.topics.slice(0, 3).map((topic, topicIndex) => (
              <ExpandedTopic topic={topic} expanded={expanded} app={props.app}/>
            ))}
          </ScrollView>
          <TouchableOpacity onPress={handlePress}>
            <View style={styles.footerContainer}>
              <Image source={require("../assets/arrow_down.png")} />
            </View>
          </TouchableOpacity>
        </View>
      )}
    </View>
  );
};



export default AppContainer;
