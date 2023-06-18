// import { StatusBar } from 'expo-status-bar';
import { StyleSheet, Text, View, SafeAreaView} from 'react-native';
import { NavigationContainer } from '@react-navigation/native';
import  AppContainer  from './containers/AppContainer';
import {useFonts} from 'expo-font'
import { GUTTER } from './theme/styles/Themes'


const response = require("./fixtures/fake_data.json");

export default function App() {  
  // const [loaded] = useFonts({
  //   // Comfortaa: require('../fonts/Comfortaa/Comfortaa-Medium.tff'),
  // })
  console.log(response.gmail.topics[0].name);
  return (
    <NavigationContainer>
      <SafeAreaView style={styles.container}>
          <View style={styles.titleContainer}>
            <Text style={styles.title}>Peeking Into</Text>
          </View>
          <AppContainer topics={response.gmail.topics}></AppContainer>
      </SafeAreaView>
    </NavigationContainer>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#000'
  },
  titleContainer: {
    marginVertical: GUTTER * 2,
    alignItems: 'center'
  },
  title: {
    fontSize: 32,
    color: "#fff",
  }
});
