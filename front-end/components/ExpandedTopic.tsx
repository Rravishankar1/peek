import React from "react";
import { View, Text, StyleSheet } from "react-native";
import { topic } from "../protos/peek";
import { backgroundColors, GUTTER, themes , appColor} from "../theme/styles/Themes";
import { useQuery } from "@apollo/client";
import { CONTINENT_QUERY } from "../gql/Query";
import { initialWindowMetrics } from "react-native-safe-area-context";

interface Props {
  topic: topic;
  expanded: boolean;
  app: string;
}


const ExpandedTopic: React.FC<Props> = (props) => {
    const [light, dark] = appColor(props.app);
    const styles = StyleSheet.create({
        container: {
          marginVertical: GUTTER,
          backgroundColor: light,
          padding: GUTTER,
          borderRadius: 15,
        },
        name: {
          //   margin:10,
          color: 'white'
        },
        nameContainer: {
            position: 'absolute',
            top: 2,
            paddingHorizontal: 15,
            paddingVertical: 1,
            backgroundColor: '#504040',
            borderRadius: 15,
            alignItems: 'center',
            justifyContent: 'center',
            width: "28%"
        },
        nameText: {
          color: "white",
          backgroundColor: "gray",
        },
        nameTextContainer: {
            backgroundColor: "gray",
        },
        textContainer: {
          flexDirection: "row",
          flexWrap: "wrap",
          // alignItems: 'center',
          // backgroundColor: "white"
          padding: 3
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
    const name = props.topic.name.length > 4 ? props.topic.name.substring(0, 4) + "..." : props.topic.name;
  return (
    // {props.expanded ?
    <View style={styles.container}>
      <View style={styles.textContainer}>
        <View style={styles.nameContainer}>
                <Text style={styles.name}>{name}</Text>
        </View>
        <Text numberOfLines={2} style={{fontSize: 15, color: 'white'}}>
            {'\t\t      '}{props.topic.summary}
        </Text>
      </View>
    </View>
  );
};



export default ExpandedTopic;
