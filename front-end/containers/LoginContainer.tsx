import React from 'react';
import {View, StyleSheet, Text, Image, Button} from 'react-native'
import * as Google from 'expo-google-app-auth';
import { StatusBar } from 'expo-status-bar';


const LoginContainer: React.FC = () => {
    const [accessToken, setAccessToken] = React.useState();
    const [userInfo, setUserInfo] = React.useState();

    async function signInWithGoogleAsync() {
        try{
            const result = await Google.logInAsync({
                androidClientId:"",
                iosClientId:"338253925414-g3b5oib6dl6es4mfasefp8kuifvdnp5n.apps.googleusercontent.com",
                // scopes: [""]
            });
            if (result.type === "success") {
                setAccessToken(accessToken);
            } else {
                console.log("Permission Denied");
            }
        } catch (e) {
            console.log(e);
        }
    }

    async function getUserData() {

    }

    function showUserInfo() {

    }

    return (
        <View style={styles.container}>
            <Image source={require('../assets/peekIcon.png')}/>
            <Button title={accessToken ? "Get User Data": "Login"} onPress={accessToken ? getUserData: signInWithGoogleAsync}/>
            <StatusBar style="auto"/>
        </View>
    );
}

const styles = StyleSheet.create({
    container: {
        flex: 1,
        alignItems: 'center',
        justifyContent: 'center',
    }
});

export default LoginContainer