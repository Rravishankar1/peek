// import { StatusBar } from 'expo-status-bar';
import { StyleSheet, Text, View } from 'react-native';
import { NavigationContainer } from '@react-navigation/native';
import  AppContainer  from './containers/AppContainer'


const response = require("./fixtures/fake_data.json");

export default function App() {  
  return (
    <NavigationContainer>
      <View style={styles.container}>
        {/* <Text>Open up App.tsx to start working on your app!</Text> */}
        <AppContainer app="gmail"></AppContainer>
        {/* <StatusBar style="auto" /> */}
      </View>
    </NavigationContainer>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#000',
    alignItems: 'center',
    justifyContent: 'center',
  },
});
