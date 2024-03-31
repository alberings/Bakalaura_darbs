(function() {
  const sendEvent = (eventData) => {
    const endpoint = 'http://127.0.0.1:8000/api/events';
    fetch(endpoint, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(eventData),
      keepalive: true
    });
  };
  
      
    // Page View and Visit Duration
    sendEvent({ type: 'pageview', path: window.location.pathname });
    window.addEventListener('unload', () => {
      sendEvent({ type: 'duration', path: window.location.pathname, duration: Date.now() - performance.timing.navigationStart });
    });
  
    // Click Tracking
    document.addEventListener('click', (e) => {
      sendEvent({ type: 'click', path: window.location.pathname, target: e.target.tagName });
    });
  
    // Scroll Depth
    window.addEventListener('scroll', () => {
      const scrolledPercentage = ((window.scrollY + window.innerHeight) / document.documentElement.scrollHeight) * 100;
      sendEvent({ type: 'scroll', path: window.location.pathname, depth: scrolledPercentage.toFixed(2) });
    });
  
    // Form Interactions - Simplified Example
    document.addEventListener('submit', (e) => {
      sendEvent({ type: 'form_submit', path: window.location.pathname, formId: e.target.id });
    });
  })();
  