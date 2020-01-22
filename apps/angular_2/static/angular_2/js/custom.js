var app = angular.module("testAngular", []);
app.controller("testAngularController", function($scope, $http, $sce) {
	var createOrNo = false
	
	$scope.saveSubject = function(item) {
		if (angular.isUndefined($scope.item)) {
    		$scope.Message = $sce.trustAsHtml("<div class='text-center'> You must select an option.</div>");		
  		} 

  		else {

			var testingData = {testing_id: $scope.item.test, images_id: imageId}

			$http.get('/api/angular_2/mixput/' + imageId).then(function successCallback(response) {
				$http.patch('/api/angular_2/mixput/' + imageId, testingData)
				$scope.Message = $sce.trustAsHtml("<div class='text-center'> Successfully updated.</div>");		
			}, function errorCallback(response) {
				$http.post('/api/angular_2/mix/', testingData)	
				$scope.Message = $sce.trustAsHtml("<div class='text-center'> Successfully added.</div>");		
			});
		}
	};
});