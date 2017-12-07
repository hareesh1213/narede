searchApp.controller('searchCtrl', function($scope, $http, $rootScope, $window) 
{
	$scope.search_results = [];
	$scope.busy = false;
	$scope.offset = 0;
	$scope.total_results = 0;
	$rootScope.total_results = 0;
	$scope.search_key = '';
	$scope.selected_suggestion = null;
	$scope.remoteUrlRequestFn = function(str) 
	{ 
		$scope.search_key = str;
		return {key: str}; 
	}
	$scope.afterSelectedMovie = function(selected)
	{
		if(selected)
		{
			$scope.selected_suggestion = selected.originalObject;
			$scope.search_key = $scope.selected_suggestion['title'];
			$scope.getResults(0);
		}
	}
	$scope.focusOut = function()
	{
		$scope.search_key = $("#search_value").val();
	}
	$rootScope.refresh = function()
	{
		location.reload();
	}
	$scope.getResults = function(type)
    {
    	if(type == 0)
    	{
    		$scope.offset = 0;
    		$scope.busy = false;
    	}
    	if(type == 1 && $scope.total_results <= ($scope.search_results).length)
    		$scope.busy = true;
    	if ($scope.busy) 
    		return false;
    	$scope.busy = true;
    	var postObj = {};
    	postObj.search_key = $scope.search_key;
    	postObj.offset = $scope.offset;
    	$http({
		        method 	: "POST",
		        url 	: $rootScope.base_url+"get-results",
		        data	: $.param(postObj),
		        headers: {'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8;'},
		    }).then(function mySuccess(response) 
		    {
		    	$scope.busy = false;
		    	var data = response.data;
		        if(data.success == true)
		        {
		        	if(type == 0)
			    	{
			    		$scope.search_results = [];
			    	}
			    	$scope.offset = $scope.offset + 10;
			    	$scope.total_results = data.total_records;
			    	$rootScope.total_results = data.total_records;
			    	$scope.searchBottmTxt = "'"+$scope.search_key+"' için "+$scope.total_results+" tane sonuç gösteriliyor.";
		        	angular.forEach(data.results, function(value, key) 
		        	{
					  	($scope.search_results).push(value);
					});
				}
		        else
		        {
		        	$scope.total_results = 0;
		        	$scope.search_results = [];
		        	$scope.searchBottmTxt = "Aradığınız film veya dizi bulunamamıştır";
		        	console.log(data.error);
		        }
		    }, 
		    function myError(error) 
		    {
		        alert(JSON.stringify(error));
		    });
    }
    $scope.open_link = function(id)
    {
    	var postObj = {};
    	postObj.auto_id = id;
    	$http({
		        method 	: "POST",
		        url 	: $rootScope.base_url+"click-count",
		        data	: $.param(postObj),
		        headers: {'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8;'},
		    }).then(function mySuccess(response) 
		    {
		    	var data = response.data;
		    }, 
		    function myError(error) 
		    {
		        alert(JSON.stringify(error));
		    });
    }
});