console.log('script running...');

new Vue({
  el: '#app',
  data: {
    cookie: ''
  },
  methods: {
    setCookie: function() {
      document.cookie = this.cookie;
    },
    redirect: function() {
      document.location.href = "/static/profile.html";
    },
    ping: function() {
      console.log('sending ping...');
      fetch('/ping')
      .then(res => {
        console.log('Response: %o');
      })
      .catch(err => {
        console.error(err);
      });
    },
    cookies: function() {
      return document.cookie;
    }
  }
});
