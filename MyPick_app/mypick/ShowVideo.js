import React, { Component } from 'react';
import {
  SafeAreaView,
  View,
  FlatList,
  StyleSheet,
  Text,
  StatusBar,
  Image,
  TouchableOpacity,
  Alert,
} from 'react-native';
import Constants from 'expo-constants';
import {
  Card,
  CardItem,
  Thumbnail,
  Container,
  Header,
  Content,
  Icon,
  Accordion,
  Left,
  Body,
  Title,
  Right,
  Button,
} from 'native-base';
import { Video } from 'expo-av';

class ShowVideo extends Component {
  render() {
    const { navigation } = this.props;
    const video_url = navigation.getParam('video_url');
    return (
      <Container>
        <Header>
          <Left>
            <TouchableOpacity
              onPress={() => {
                navigation.goBack();
              }}>
              <Text style={{ alignItems: 'center' }}>BACK</Text>
            </TouchableOpacity>
          </Left>
          <Body>
            <Title>My pick!</Title>
          </Body>
          <Right />
        </Header>
        <Video
          source={{
            uri: video_url,
          }}
          rate={1.0}
          volume={1.0}
          isMuted={false}
          resizeMode="cover"
          shouldPlay
          isLooping
          style={{ flex: 1 }}
        />
      </Container>
    );
  }
}

export default ShowVideo;
