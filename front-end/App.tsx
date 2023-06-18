// import { StatusBar } from 'expo-status-bar';
import { StyleSheet, Text, View, SafeAreaView} from 'react-native';
import { NavigationContainer } from '@react-navigation/native';
import  AppContainer  from './containers/AppContainer';
import {useFonts} from 'expo-font';
import { GUTTER } from './theme/styles/Themes';
import { peekRequest, peekRequest_app } from './protos/peek';
import { ApolloClient, InMemoryCache, ApolloProvider } from '@apollo/client';

// Initialize Apollo Client
const client = new ApolloClient({
  uri: 'https://countries.trevorblades.com/graphql',
  cache: new InMemoryCache()
});



const response = require("./fixtures/fake_data.json");
// const client = new peekServiceClient('http://localhost:50051');
// const request: peekRequest = {
//   userID: 0,
//   appID: peekRequest_app.GMAIL,
  
// }

export default function App() {  
  console.log(response.gmail.topics[0].name);
  // console.log(data)
  return (
    <ApolloProvider client={client}>
      <NavigationContainer>
        <SafeAreaView style={styles.container}>
            <View style={styles.titleContainer}>
              <Text style={styles.title}>Peeking Into</Text>
            </View>
            <AppContainer topics={response.gmail.topics}></AppContainer>
        </SafeAreaView>
      </NavigationContainer>
    </ApolloProvider>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#000',
    height: "100%",
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
