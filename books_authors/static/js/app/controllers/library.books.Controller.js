'use strict';

library.controller('booksCtrl', function ($scope, $http) {

    // Initialization
    $scope.title = '';
    $scope.author = '';
    $scope.annotation = '';
    $scope.genre = [];
    $scope.slug = '';

    // GET method
    $http
        .get('/api/books/?format=json')
        .success(function (out_data) {
            console.log(JSON.stringify(out_data));
        });

});