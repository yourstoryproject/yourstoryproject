import EmberRouter from '@ember/routing/router';
import config from './config/environment';

const Router = EmberRouter.extend({
  location: config.locationType,
  rootURL: config.rootURL
});

Router.map(function() {
  this.route('home');
  this.route('tag');
  this.route('not-found', { path: '/*path' });
  this.route('account');
});

export default Router;
Router.map(function() {
});
