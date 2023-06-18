import React, { useState } from "react";
import {
  StyleProp,
  View,
  StyleSheet,
  Text,
  Image,
  ScrollView,
  TouchableOpacity,
} from "react-native";
import { useNavigation } from "@react-navigation/native";
import { themes, GUTTER } from "../theme/styles/Themes";
import { topic } from "../protos/peek";
import Topic from "../components/Topic";
import ExpandedTopic from "../components/ExpandedTopic";
import { isPropertySignature } from "typescript";

interface Props {
  topics: topic[];
}

const app = (app_name: string) => {
  switch (app_name) {
    case "gmail":
      return "../assets/social_icons/gmail.png";
  }
};

// Text.defaultProps.style = {

// }

const AppContainer: React.FC<Props> = (props) => {
  // const background_color=themes[props.app];
  const img = require("../assets/social_icons/gmail.png");
  const totalNotifs = props.topics.reduce(
    (accumulator, currentValue) => accumulator + currentValue.notifs.length,
    0
  );
  const [expanded, setExpanded] = useState(true);
  const handlePress = () => {
    setExpanded(!expanded);
  };
  const containerStyle = expanded ? styles.container : styles.containerExpanded;
  return (
    <View style={styles.flexOne}>
      {expanded === true ? (
        <TouchableOpacity onPress={handlePress} style={styles.container}>
          {/* // <View style={styles.container}> */}
          <View style={styles.titleLogoContainer}>
            <Image source={img} />
            <View style={styles.titleContainer}>
              <Text style={styles.title}>Inbox</Text>
            </View>
          </View>
          <ScrollView style={styles.topicContainer}>
            {props.topics.map((topic, topicIndex) => (
              <Topic topic={topic} expanded={expanded} />
            ))}
          </ScrollView>
          <View style={styles.footerContainer}>
            <View style={styles.notificationsNumberContainer}>
              <Text style={{ color: "white", fontSize: 20 }}>
                {totalNotifs}
              </Text>
            </View>
            <View style={styles.footerTextContainer}>
              <Text style={{ color: "white", fontSize: 20 }}>
                Notifcations Received Since Last Opened
              </Text>
            </View>
          </View>
        </TouchableOpacity>
      ) : (
        <TouchableOpacity onPress={handlePress} style={[styles.container, expandedStyles.container]}>
          <View style={styles.titleLogoContainer}>
            <Image source={img} />
            <View style={styles.titleContainer}>
              <Text style={styles.title}>Inbox</Text>
            </View>
          </View>
          <ScrollView style={[styles.topicContainer, expandedStyles.topicContainer]}>
            {props.topics.map((topic, topicIndex) => (
              <ExpandedTopic topic={topic} expanded={expanded} />
            ))}
          </ScrollView>
          <View style={styles.footerContainer}>
            <View style={styles.notificationsNumberContainer}>
              <Text style={{ color: "white", fontSize: 20 }}>
                {totalNotifs}
              </Text>
            </View>
            <View style={styles.footerTextContainer}>
              <Text style={{ color: "white", fontSize: 20 }}>
                Notifcations Received Since Last Opened
              </Text>
            </View>
          </View>
        </TouchableOpacity>
      )}
    </View>
  );
};

const expandedStyles = StyleSheet.create({
    container: {
        flex: 0,
    },
    topicContainer: {
        backgroundColor: 'transparent'
    }
})

const styles = StyleSheet.create({
  container: {
    backgroundColor: themes.gmail_dark,
    borderRadius: 25,
    flex: 1,
    // paddingVertical: GUTTER
  },
  containerExpanded: {
    backgroundColor: "black",
    borderRadius: 25,
    // flex: 1,
  },
  titleContainer: {
    backgroundColor: themes.gmail_light,
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
    backgroundColor: themes.gmail_light,
    marginHorizontal: GUTTER * 2,
    borderRadius: 15,
  },
  flexOne: {
    flex: 1,
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
    backgroundColor: themes.gmail_light,
    height: 30,
    width: 30,
  },
});

export default AppContainer;
