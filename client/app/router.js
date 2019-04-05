import EmberRouter from '@ember/routing/router';
import config from './config/environment';

const Router = EmberRouter.extend({
  location: config.locationType,
  rootURL: config.rootURL
});

Router.map(function() {
  this.route('home');
  this.route('tag');
});

export default Router;

Router.map(function() {
  this.route('login');
  this.route('authenticated', {path: ''}, function() {
    this.route('account');
  });
  this.route('not-found', { path: '/*path' });

});
