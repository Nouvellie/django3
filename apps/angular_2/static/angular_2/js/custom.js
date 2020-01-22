var app = angular.module("testAngular", []);
app.controller("testAngularController", function($scope, $http) {
	var createOrNo = false
	$scope.mainDict = {};

	$scope.saveSubject = function(item) {
		var testingData = {testing_id: $scope.item.test, images_id: imageId}

		$http.get('/api/angular_2/mixput/' + imageId).then(function successCallback(response) {
			$http.patch('/api/angular_2/mixput/' + imageId, testingData)
		}, function errorCallback(response) {
			$http.post('/api/angular_2/mix/', testingData)	
		});
	};

});