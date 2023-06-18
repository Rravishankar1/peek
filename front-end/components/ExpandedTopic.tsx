import React from "react";
import { View, Text, StyleSheet } from "react-native";
import { topic } from "../protos/peek";
import { GUTTER, themes } from "../theme/styles/Themes";
import { useQuery } from "@apollo/client";
import { CONTINENT_QUERY } from "../gql/Query";
import { initialWindowMetrics } from "react-native-safe-area-context";

interface Props {
  topic: topic;
  expanded: boolean;
}

const ExpandedTopic: React.FC<Props> = (props) => {
  const { loading, error, data } = useQuery(CONTINENT_QUERY);
  return (
    // {props.expanded ?
    <View style={styles.container}>
      <View style={styles.textContainer}>
        <Text>
          <View>
            <Text>{props.topic.name}</Text>
          </View>
          {props.topic.summary}
        </Text>
      </View>
    </View>
  );
};

const styles = StyleSheet.create({
  container: {
    marginVertical: GUTTER,
    backgroundColor: themes.gmail_light,
    padding: GUTTER,
    borderRadius: 15,
  },
  nameText: {
    color: "white",
    backgroundColor: "gray",
  },
  textContainer: {
    flexDirection: "row",
    flexWrap: "wrap",
    alignItems: 'center'
  },
  topicText: {
    color: "#fff",
    fontSize: 20,
  },
  summaryContainer: {
    // marginVertical: GUTTER * 2,
    marginHorizontal: GUTTER * 1.5,
  },
  summaryText: {
    color: "white",
  },
});

export default ExpandedTopic;
