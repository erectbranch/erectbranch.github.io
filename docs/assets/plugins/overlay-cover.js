document.addEventListener('DOMContentLoaded', () => {
    const canvas = document.getElementById('globe');
    const ctx = canvas.getContext('2d');
    
    // Set canvas size
    const setCanvasSize = () => {
      const size = Math.min(window.innerWidth * 0.8, window.innerHeight * 0.6);
      canvas.width = size;
      canvas.height = size;
    };
    
    setCanvasSize();
    window.addEventListener('resize', setCanvasSize);
    
    // Globe parameters
    const radius = canvas.width * 0.4;
    let rotationSpeed = 0.005;
    // Initial rotation to make north pole face northeast
    let rotationX = -Math.PI / 4; // -45 degrees to tilt the globe
    let rotationY = Math.PI / 4;  // 45 degrees to turn the globe
    let isRotating = true;
    let isDragging = false;
    let lastMouseX, lastMouseY;
    
    // Create wireframe data
    const createGlobe = () => {
      const points = [];
      const lines = [];
      
      // Create latitude lines
      const latitudeCount = 15;
      for (let i = 0; i < latitudeCount; i++) {
        const phi = Math.PI * i / (latitudeCount - 1);
        const latitudePoints = [];
        
        const longitudeCount = 30;
        for (let j = 0; j <= longitudeCount; j++) {
          const theta = 2 * Math.PI * j / longitudeCount;
          const x = radius * Math.sin(phi) * Math.cos(theta);
          const y = radius * Math.cos(phi);
          const z = radius * Math.sin(phi) * Math.sin(theta);
          
          latitudePoints.push({ x, y, z });
        }
        
        for (let j = 0; j < latitudePoints.length - 1; j++) {
          lines.push([latitudePoints[j], latitudePoints[j + 1]]);
        }
      }
      
      // Create longitude lines
      const longitudeCount = 15;
      for (let i = 0; i < longitudeCount; i++) {
        const theta = 2 * Math.PI * i / longitudeCount;
        const longitudePoints = [];
        
        const latitudeCount = 30;
        for (let j = 0; j <= latitudeCount; j++) {
          const phi = Math.PI * j / latitudeCount;
          const x = radius * Math.sin(phi) * Math.cos(theta);
          const y = radius * Math.cos(phi);
          const z = radius * Math.sin(phi) * Math.sin(theta);
          
          longitudePoints.push({ x, y, z });
        }
        
        for (let j = 0; j < longitudePoints.length - 1; j++) {
          lines.push([longitudePoints[j], longitudePoints[j + 1]]);
        }
      }
      
      return { lines };
    };
    
    const globe = createGlobe();
    
    // Rotate a point around the X and Y axes
    const rotatePoint = (point, rotX, rotY) => {
      // Rotate around Y axis
      let x1 = point.x * Math.cos(rotY) - point.z * Math.sin(rotY);
      let z1 = point.z * Math.cos(rotY) + point.x * Math.sin(rotY);
      
      // Rotate around X axis
      let y2 = point.y * Math.cos(rotX) - z1 * Math.sin(rotX);
      let z2 = z1 * Math.cos(rotX) + point.y * Math.sin(rotX);
      
      return { x: x1, y: y2, z: z2 };
    };
    
    // Draw text in a circle around the globe
    const drawCircularText = () => {
      const text = "AI research with a global perspective. Pioneering ";
      const centerX = canvas.width / 2;
      const centerY = canvas.height / 2;
      const textRadius = radius * 1.2; // Slightly larger than the globe
      
      ctx.save();
      ctx.font = "bold 24px serif";  // custom: 와이어 프레임을 감싼 텍스트 폰트(Arial -> serif) 및 크기 변경
      ctx.textAlign = "center";
      ctx.textBaseline = "middle";
      ctx.fillStyle = "#0f5acb";     // custom: 와이어 프레임을 감싼 텍스트 색상 변경
      
      const angleStep = (2 * Math.PI) / text.length;
      
      for (let i = 0; i < text.length; i++) {
        const angle = i * angleStep;
        
        ctx.save();
        ctx.translate(
          centerX + Math.cos(angle) * textRadius,
          centerY + Math.sin(angle) * textRadius
        );
        ctx.rotate(angle + Math.PI / 2); // Rotate text to face outward
        ctx.fillText(text[i], 0, 0);
        ctx.restore();
      }
      
      ctx.restore();
    };
    
    // Draw the globe
    const drawGlobe = () => {
      ctx.clearRect(0, 0, canvas.width, canvas.height);
      
      // Set line style
      ctx.strokeStyle = '#e14630';    // custom: 와이퍼 프레임 선 색상 변경
      ctx.lineWidth = 1;
      
      // Draw each line
      globe.lines.forEach(line => {
        const p1 = rotatePoint(line[0], rotationX, rotationY);
        const p2 = rotatePoint(line[1], rotationX, rotationY);
        
        // Simple depth effect - lines further back are more transparent
        const depth1 = (p1.z + radius) / (2 * radius);
        const depth2 = (p2.z + radius) / (2 * radius);
        const avgDepth = (depth1 + depth2) / 2;
        
        ctx.beginPath();
        ctx.moveTo(canvas.width / 2 + p1.x, canvas.height / 2 + p1.y);
        ctx.lineTo(canvas.width / 2 + p2.x, canvas.height / 2 + p2.y);
        
        // Adjust opacity based on depth
        ctx.globalAlpha = 0.2 + avgDepth * 0.8;
        ctx.stroke();
        ctx.globalAlpha = 1;
      });
      
      // Draw the circular text
      drawCircularText();
    };
    
    // Animation loop
    const animate = () => {
      if (isRotating) {
        // Rotate around the vertical axis
        const rotationAxis = {
          x: Math.sin(Math.PI/4), // 45 degrees
          y: 0,
          z: Math.cos(Math.PI/4)
        };
        
        // Apply rotation around the custom axis
        rotationY += rotationSpeed;
      }
      
      drawGlobe();
      requestAnimationFrame(animate);
    };
    
    // Start animation
    animate();
    
    // Mouse interaction
    canvas.addEventListener('mousedown', (e) => {
      isDragging = true;
      lastMouseX = e.clientX;
      lastMouseY = e.clientY;
    });
    
    canvas.addEventListener('mousemove', (e) => {
      if (isDragging) {
        const deltaX = e.clientX - lastMouseX;
        const deltaY = e.clientY - lastMouseY;
        
        rotationY += deltaX * 0.005;
        rotationX += deltaY * 0.005;
        
        lastMouseX = e.clientX;
        lastMouseY = e.clientY;
      }
    });
    
    canvas.addEventListener('mouseup', () => {
      isDragging = false;
    });
    
    canvas.addEventListener('mouseleave', () => {
      isDragging = false;
    });
    
    // Touch interaction
    canvas.addEventListener('touchstart', (e) => {
      if (e.touches.length === 1) {
        isDragging = true;
        lastMouseX = e.touches[0].clientX;
        lastMouseY = e.touches[0].clientY;
      }
    });
    
    canvas.addEventListener('touchmove', (e) => {
      if (isDragging && e.touches.length === 1) {
        const deltaX = e.touches[0].clientX - lastMouseX;
        const deltaY = e.touches[0].clientY - lastMouseY;
        
        rotationY += deltaX * 0.005;
        rotationX += deltaY * 0.005;
        
        lastMouseX = e.touches[0].clientX;
        lastMouseY = e.touches[0].clientY;
        
        e.preventDefault(); // Prevent scrolling
      }
    });
    
    canvas.addEventListener('touchend', () => {
      isDragging = false;
    });
    
    // Control buttons
    document.getElementById('slowDown').addEventListener('click', () => {
      rotationSpeed = Math.max(0.001, rotationSpeed - 0.002);
    });
    
    document.getElementById('speedUp').addEventListener('click', () => {
      rotationSpeed = Math.min(0.02, rotationSpeed + 0.002);
    });
    
    document.getElementById('toggleRotation').addEventListener('click', () => {
      isRotating = !isRotating;
      document.getElementById('toggleRotation').textContent = isRotating ? '❚❚' : '▶';
    });

    // 오버레이 제거 기능 추가
    document.getElementById('closeOverlay').addEventListener('click', function() {
      // 단순 오버레이 제거
      // document.getElementById('overlay').style.display = 'none';
      const overlay = document.getElementById('overlay');
      
      // 오버레이 희미해지는 애니메이션 시작
      overlay.classList.add('fade-out');
      
      // 애니메이션이 끝난 후 오버레이를 완전히 제거
      overlay.addEventListener('transitionend', function() {
        overlay.style.display = 'none';
      }, { once: true });
    });
    
  });