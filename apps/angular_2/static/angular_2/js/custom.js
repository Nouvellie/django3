var app = angular.module('testAngular', []);
app.controller('testAngularController', function($scope, $http) {
	// $scope.testAngularList = [{testAngularText: 'Finish this app.', done: false}];
	$http.get('/api/angular_1/').then(function(response) {
		$scope.testAngularList = [];
		for (var i = 0; i < response.data.length; i++) {
			var tests = {};
			tests.testAngularText = response.data[i].test_angular_text
			tests.done = response.data[i].test_angular_bool
			tests.id = response.data[i].test_angular_id
			$scope.testAngularList.push(tests);
		}
	});
	$scope.testAngularAdd = function() {
		$scope.testAngularList.push({testAngularText: $scope.testAngularInput, done: false});
		$scope.testAngularInput = '';
	};
	$scope.saveData = function() {
		var data = {test_angular_text: $scope.testAngularInput, test_angular_bool: false}
		$http.put('/api/angular_1/', data)
	};
	$scope.remove = function() {
		var currentList = $scope.testAngularList;
		$scope.testAngularList = [];
		angular.forEach(currentList, function(tests) {
			if (tests.done) {
				$http.delete('/api/angular_1/' + tests.id + '/');
			}	
			else {
				$scope.testAngularList.push(tests);
			}
		})
	}
})