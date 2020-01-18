var app = angular.module('testAngular', []);
app.controller('testAngularController', ['$scope', function($scope) {
	$scope.mainDict = {};
	console.log(item);
	$scope.saveSubject = function(item) {
		$scope.mainDict = angular.copy(item);
		console.log(item);
	};
}

https://stackoverflow.com/questions/35061614/django-angular-form-submit