var searchApp = angular.module('searchApp', ['ui.router', 'infinite-scroll', 'angucomplete-alt']);
//angular.module('infinite-scroll').value('THROTTLE_MILLISECONDS', 250)
searchApp.run(function($rootScope) 
{
    $rootScope.base_url = 'http://52.26.166.124/api/';
    $rootScope.site_url = 'http://52.26.166.124/#!/';
    $rootScope.currencySymbol = "TL";
});
searchApp.config(function($stateProvider, $urlRouterProvider) 
{
    $urlRouterProvider.otherwise('/');
    $stateProvider
    .state('index', 
    {
        url: '/',
        controller: "searchCtrl",
        templateUrl: 'templates/index.html'
    })
});
searchApp.filter('toArray', function () 
{
  return function (obj, addKey) {
    if (!angular.isObject(obj)) return obj;
    if ( addKey === false ) {
      return Object.keys(obj).map(function(key) {
        return obj[key];
      });
    } else {
      return Object.keys(obj).map(function (key) {
        var value = obj[key];
        return angular.isObject(value) ?
          Object.defineProperty(value, '$key', { enumerable: false, value: key}) :
          { $key: key, $value: value };
      });
    }
  };
});