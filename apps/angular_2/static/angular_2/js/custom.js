var app = angular.module("testAngular", []);
app.controller("testAngularController", function($scope, $http) {
	var createOrNo = false
	$scope.mainDict = {};
	$http.get('api/angular_2/mixput/' + imageId + '/').then(
		function successCallback(response){
			console.log("yes");
			console.log(response);
		}, function errorCallback(response){
			// $http.get()
			console.log("no");
			createOrNo = true
			if (createOrNo == true) {
				console.log('true');
			}
		});
	$scope.saveSubject = function(item) {
		var testingData = {testing_id: $scope.item.test, images_id: imageId}
		console.log(testingData);
		
		
		$http.post('/api/angular_2/mix/', testingData).then(function successCallback(response){
			console.log("yes");
			console.log(response);
		}, function errorCallback(response){
			// $http.get()
			console.log("no");
			console.log(response);
		});
	
		// $http
	};

});