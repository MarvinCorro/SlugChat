var slugChatApp = angular.module('slugChatApp', []);

slugChatApp.controller('testDataCtrl', function ($scope) {
  $scope.messages = [
    {'name': 'Your Boss',
     'subject': "You're fired",
    'time': "2 mins",
     'profile': "http://i.forbesimg.com/media/lists/people/anna-wintour_416x416.jpg",},
     {'name': 'Your Mom',
      'subject': "Call me sweetie",
     'time': "500 years",
      'profile': "http://img.thesun.co.uk/aidemitlum/archive/00787/Susan-Boyle280_787960a-144x217.jpg",},
      {'name': "Marvin's Twin",
       'subject': "Tickets to concert!",
      'time': "3 hours",
       'profile': "../static/images/MarvinCorroProfileIm.jpg",},
       {'name': 'Your Husband',
        'subject': "I'm gonna be late.",
       'time': "1 min",
        'profile': "http://i2.wp.com/www.powerlineblog.com/ed-assets/2016/01/donald-trump.jpg?fit=1200%2C1200",},
        {'name': 'James Jiggles',
         'subject': "Once I was...",
        'time': "7 years old",
         'profile': "../static/AdminLTE/dist/img/user2-160x160.jpg",},
  ];

  $scope.classrooms = [
    {'name': "CMPS 115", 'description':"Software Engineering"},
    {'name': "CMPE 110", 'description':"Computer Architecture"},
    {'name': "CMPS 109", 'description':"Advanced Programming"}
  ];

  $scope.classmates = [
    {'name': "Chris Kyle", 'profile':"../static/img/profile-pic.png"},
    {'name': "Aramis Marden", 'profile':"../static/img/profile-pic.png"},
    {'name': "Joseph Faulkner", 'profile':"../static/img/profile-pic.png"},
    {'name': "Christopher Ketchum", 'profile':"../static/img/profile-pic.png"},
    {'name': 'Snow White', 'profile':"../static/img/profile-pic.png"},
    {'name': "Alex Pang", 'profile':"../static/img/profile-pic.png"}
  ];

  $scope.userinfo =
    {'username': "Martin Corro",
    'profile': "../static/images/MarvinCorroProfileIm.jpg",
    'bio': "I like looting, shooting, bootin and computing.",
    'title': "Student",
    'contactinfo' : "C:(555)-555-5555",
  };



});
