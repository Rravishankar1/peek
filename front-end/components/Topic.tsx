import React from 'react';
import {View, Text, StyleSheet} from 'react-native';
import { topic } from '../protos/peek';
import {GUTTER, themes} from "../theme/styles/Themes";

interface Props {
    topic: topic;
}

const Topic: React.FC<Props> = props => {
    return (
        <View style={styles.container}>
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
    );
}

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
        backgroundColor: themes.gmail_dark,
        paddingVertical: GUTTER * 0.5,
        paddingHorizontal: GUTTER * 2,
        // alignItems: 'space-between',
    },
    topicText: {
        color: "#fff",
        fontSize: 20
    },
    summaryContainer: {
        // marginVertical: GUTTER * 2,
        marginHorizontal: GUTTER * 1.5,
    },
    summaryText: {
        color: 'white'
    }
});


export default Topic;