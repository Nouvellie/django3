var app = angular.module("testAngular", []);
app.controller("testAngularController", function($scope, $http, $sce, $timeout) {
	var createOrNo = false
	$http.get('/api/angular_2/testing/').then(function(response){
		var tito = response.data;
		
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