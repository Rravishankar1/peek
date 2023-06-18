import React from 'react';
import {View, Text, StyleSheet} from 'react-native';
import { topic } from '../protos/peek';
import {GUTTER, themes, appColor} from "../theme/styles/Themes";
import { useQuery } from "@apollo/client";
import { CONTINENT_QUERY } from "../gql/Query";

interface Props {
    topic: topic;
    expanded: boolean;
    app: string;

}


const Topic: React.FC<Props> = props => {
    const [_, dark] = appColor(props.app);
    const expandedStyles = StyleSheet.create({
        container: {
            marginVertical: GUTTER,
        }
    });
    
    const styles = StyleSheet.create({
        container: {
            // marginHorizontal: GUTTER * 2,
            marginVertical: GUTTER,
        },
        emojiText: {
            fontSize: 40,
        },
        nameContainer: {
            flexDirection: "row",
            alignItems: "center",
            justifyContent: "space-between",
            marginHorizontal: GUTTER
        },
        nameTextContainer: {
            borderRadius: 12,
            backgroundColor: dark,
            marginVertical: GUTTER * 0.5,
            paddingVertical: GUTTER * 0.5,
            paddingHorizontal: GUTTER * 2,
            width: "75%",
            // alignItems: 'space-between',
        },
        topicText: {
            color: "#fff",
            fontSize: 15
        },
        summaryContainer: {
            // marginVertical: GUTTER * 2,
            marginHorizontal: GUTTER * 1.5,
        },
        summaryText: {
            color: 'white'
        }
    });
    return (
        // {props.expanded ? 
        <View style={styles.container}>
            {props.expanded === true ? 
                <View>
                <View style={styles.nameContainer}>
                    <View style={styles.nameTextContainer}>
                        <Text style={styles.topicText}>{props.topic.name}</Text> 
                    </View>
                    <Text style={styles.emojiText}> {props.topic.emoji} </Text>
                </View>
                <View style={styles.summaryContainer}>
                    <Text style={styles.summaryText}>{props.topic.summary}</Text>
                </View> 
            </View>
            : 
            <View style={expandedStyles.container}>
                <Text>hello</Text>
            </View>}
        </View> 
    );
}




export default Topic;
