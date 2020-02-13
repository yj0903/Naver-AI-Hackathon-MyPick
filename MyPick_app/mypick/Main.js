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

const DATA = [
  {
    id: 'blackpink',
    title: '3주년',
    date: 'Feb 14, 2020',
    profile_img:
      'https://d1yjjnpx0p53s8.cloudfront.net/styles/logo-thumbnail/s3/052017/untitled-1_9.png?itok=3xjaxvLi',
    contents_url: 'https://i.imgur.com/jlErwF7.png',
  },
  {
    id: 'neverdie',
    title: 'Never die@@@@',
    date: 'Feb 13, 2020',
    profile_img: 'https://i.imgur.com/k94jwRt.jpg',
    contents_url:
      'https://i.pinimg.com/564x/2b/98/d8/2b98d826e278f203867a2277abc23850.jpg',
  },
];

function Item({ title, profile_img, contents_url, date }) {
  return (
    <Card>
      <CardItem>
        <Left>
          <Thumbnail
            source={{
              uri: profile_img,
            }}
          />
          <Body>
            <Text>{title}</Text>
            <Text note>{date}</Text>
          </Body>
        </Left>
      </CardItem>
      <CardItem cardBody>
        <Image
          source={{
            uri: contents_url,
          }}
          style={{ height: 200, width: null, flex: 1 }}
        />
      </CardItem>
      <CardItem style={{ height: 45 }}>
        <Left>
          <Button transparent>
            <Icon name="ios-heart" style={{ color: 'black' }} />
          </Button>
          <Button transparent>
            <Icon name="ios-chatbubbles" style={{ color: 'black' }} />
          </Button>
          <Button transparent>
            <Icon name="ios-send" style={{ color: 'black' }} />
          </Button>
        </Left>
      </CardItem>
    </Card>
  );
}

class Main extends Component {
  render() {
    const { navigation } = this.props;

    return (
      <Container>
        <Header>
          <Left>
            <Icon name="ios-menu" style={{ paddingLeft: 10 }} />
          </Left>
          <Body>
            <Title>My pick!</Title>
          </Body>
          <Right>
            <Icon name="ios-send" style={{ paddingRight: 10 }} />
          </Right>
        </Header>
        <SafeAreaView style={styles.container}>
          <FlatList
            data={DATA}
            renderItem={({ item }) => (
              <TouchableOpacity
                onPress={() => {
                  navigation.navigate('ShowGroupList', {
                    group_name: item.id,
                  });
                }}>
                <Item
                  title={item.title}
                  url={item.url}
                  profile_img={item.profile_img}
                  contents_url={item.contents_url}
                  date={item.date}
                />
              </TouchableOpacity>
            )}
            keyExtractor={item => item.id}
          />
        </SafeAreaView>
      </Container>
    );
  }
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
  },
});

export default Main;
