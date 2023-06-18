import React from "react";
import { StyleProp, View, StyleSheet, Text, Image, ScrollView} from "react-native";
import { useNavigation } from "@react-navigation/native";
import {themes, GUTTER} from "../theme/styles/Themes";
import {topic} from "../protos/peek";
import Topic from "../components/Topic";
import { isPropertySignature } from "typescript";



interface Props {
    topics: topic[];
}

const app = (app_name: string) => {
    switch(app_name) {
        case "gmail": 
            return "../assets/social_icons/gmail.png";
    }

}

// Text.defaultProps.style = {

// }

const AppContainer: React.FC<Props> = props => {
    // const background_color=themes[props.app];
    const img = require("../assets/social_icons/gmail.png");
    const totalNotifs = props.topics.reduce(
        (accumulator, currentValue) => accumulator + currentValue.notifs.length,
        0
    )
    return (
        <View style={styles.container}>
            <View style={styles.titleLogoContainer}>
                <Image source={img}/>
                <View style={styles.titleContainer}>
                    <Text style={styles.title}>Inbox</Text>
                </View>
            </View>
            <ScrollView style={styles.topicContainer}>
                {props.topics.map((topic, topicIndex) => (
                    <Topic topic={topic}/>
                ))}
            </ScrollView>
            <View style={styles.footerContainer}>
                <View style={styles.notificationsNumberContainer}>
                    <Text style={{color: 'white', fontSize: 20}}>{totalNotifs}</Text>
                </View>
                <View style={styles.footerTextContainer}>
                    <Text style={{color: 'white', fontSize: 20}}>Notifcations Received Since Last Opened</Text>
                </View>
            </View>
        </View>
    );
}

const styles = StyleSheet.create({
    container: {
        backgroundColor: themes.gmail_dark,
        borderRadius: 25,
        flex: 1,
        // paddingVertical: GUTTER
    },
    titleContainer: {
        backgroundColor: themes.gmail_light,
        borderRadius: 15,
        marginHorizontal: GUTTER * 2,
        paddingHorizontal: GUTTER * 2,
        paddingVertical: GUTTER,
    },
    titleLogoContainer: {
        flexDirection: 'row',
        alignItems: 'center',
        justifyContent: 'center',
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
        alignItems: 'center',
    },
    footerTextContainer: {
        marginVertical: GUTTER,
    },
    notificationsNumberContainer: {
        justifyContent: 'center',
        alignItems: 'center',
        borderRadius: 20,
        backgroundColor: themes.gmail_light,
        height: 30,
        width: 30,
    }
})

export default AppContainer;