  function checkmesages() {
    try {
      var xmlobj = new XMLHttpRequest();
    } catch (e) {
      var xmlobj = new ActiveXObject();
    } finally {
      var msgcount = 0;
    }
  }
