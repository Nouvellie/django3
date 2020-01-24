var app = angular.module("testAngular", []);
app.config(function($interpolateProvider) {
	$interpolateProvider.startSymbol('{$');
    $interpolateProvider.endSymbol('$}');
});
app.controller("testAngularController", function($scope, $http, $sce, $timeout) {
	$scope.createOrNo = 'Enter a name:';
	$http.get('/api/angular_2/testing/').then(function(response) {
		
		$scope.testAngularList = [];
		for (var i = 0; i < response.data.length; i++) {
			var tests = {};
			tests.testAngularText = response.data[i].testing_id
			tests.done = response.data[i].testing_name
			$scope.testAngularList.push(tests);
		}
	});
	$http.get('/api/angular_2/mix').then(function(response) {
		$scope.mixes = [];
		for (var i = 0; i < response.data.length; i++) {
			
			if (response.data[i].images_id == imageId) {
				$scope.mixes.push(
					{"images_id": imageId, "testing_id": response.data[i]},
					{key: "testing_id", value: response.data[i].testing_id}
				)
				console.log($scope.mixes);
			}
			
		}
	});
	
	$scope.saveSubject = function(item) {
		if (angular.isUndefined($scope.item)) {
			$scope.Message = $sce.trustAsHtml("<div class='text-center' style='color: red;'> You must select an option.</div>");			
			$timeout(function() {
				$scope.Message = $sce.trustAsHtml("");			
			}, 3000);
  		} 

  		else {

			var testingData = {testing_id: $scope.item.test, images_id: imageId}

			$http.get('/api/angular_2/mixput/' + imageId).then(function successCallback(response) {
				$http.patch('/api/angular_2/mixput/' + imageId, testingData)
				$scope.Message = $sce.trustAsHtml("<div class='text-center' style='color: blue;'> Successfully updated.</div>");		
				$timeout(function() {
					$scope.Message = $sce.trustAsHtml("");			
				}, 3000);
			}, function errorCallback(response) {
				$http.post('/api/angular_2/mix/', testingData)	
				$scope.Message = $sce.trustAsHtml("<div class='text-center' style='color: blue;'> Successfully added.</div>");		
				$timeout(function() {
					$scope.Message = $sce.trustAsHtml("");			
				}, 3000);
			});
		}
	};
});