var app = angular.module("testAngular", []);
app.controller("testAngularController", ['$scope', function($scope, $http) {
	$scope.mainDict = {};
	$scope.saveSubject = function() {
		var testingData = {testasd: $scope.item.test, aux: false, imagenumber: imageId}
		console.log(testingData);
		// $http
	};

}]);