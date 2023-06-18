import React from "react";
import { StyleProp, View, StyleSheet, Text} from "react-native";
import { useNavigation } from "@react-navigation/native";
import {themes, GUTTER} from "../theme/styles/Themes";


interface Props {
    app: string
}

const AppContainer: React.FC<Props> = props => {
    // const background_color=themes[props.app];
    return (
        <View style={styles.container}>
            <Text>Hello</Text>
        </View>
    );
}

const styles = StyleSheet.create({
    container: {
        backgroundColor: themes.gmail_dark,
    }
})

export default AppContainer;