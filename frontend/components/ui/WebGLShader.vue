<template>
  <canvas ref="canvasRef" class="fixed top-0 left-0 w-full h-full block" />
</template>

<script setup lang="ts">
import { ref, onMounted, onUnmounted } from 'vue'
import * as THREE from 'three'

const canvasRef = ref<HTMLCanvasElement | null>(null)

let scene: THREE.Scene | null = null
let camera: THREE.OrthographicCamera | null = null
let renderer: THREE.WebGLRenderer | null = null
let mesh: THREE.Mesh | null = null
let uniforms: any = null
let animationId: number | null = null

const vertexShader = `
  attribute vec3 position;
  void main() {
    gl_Position = vec4(position, 1.0);
  }
`

const fragmentShader = `
  precision highp float;
  uniform vec2 resolution;
  uniform float time;
  uniform float xScale;
  uniform float yScale;
  uniform float distortion;

  void main() {
    vec2 p = (gl_FragCoord.xy * 2.0 - resolution) / min(resolution.x, resolution.y);
    
    float d = length(p) * distortion;
    
    float rx = p.x * (1.0 + d);
    float gx = p.x;
    float bx = p.x * (1.0 - d);

    float r = 0.05 / abs(p.y + sin((rx + time) * xScale) * yScale);
    float g = 0.05 / abs(p.y + sin((gx + time) * xScale) * yScale);
    float b = 0.05 / abs(p.y + sin((bx + time) * xScale) * yScale);
    
    gl_FragColor = vec4(r, g, b, 1.0);
  }
`

function handleResize() {
  if (!renderer || !uniforms) return
  const width = window.innerWidth
  const height = window.innerHeight
  renderer.setSize(width, height, false)
  uniforms.resolution.value = [width, height]
}

function animate() {
  if (uniforms) uniforms.time.value += 0.01
  if (renderer && scene && camera) {
    renderer.render(scene, camera)
  }
  animationId = requestAnimationFrame(animate)
}

onMounted(() => {
  if (!canvasRef.value) return

  scene = new THREE.Scene()
  renderer = new THREE.WebGLRenderer({ canvas: canvasRef.value })
  renderer.setPixelRatio(window.devicePixelRatio)
  renderer.setClearColor(new THREE.Color(0x000000))

  camera = new THREE.OrthographicCamera(-1, 1, 1, -1, 0, -1)

  uniforms = {
    resolution: { value: [window.innerWidth, window.innerHeight] },
    time: { value: 0.0 },
    xScale: { value: 1.0 },
    yScale: { value: 0.5 },
    distortion: { value: 0.05 },
  }

  const position = [
    -1.0, -1.0, 0.0,
     1.0, -1.0, 0.0,
    -1.0,  1.0, 0.0,
     1.0, -1.0, 0.0,
    -1.0,  1.0, 0.0,
     1.0,  1.0, 0.0,
  ]

  const positions = new THREE.BufferAttribute(new Float32Array(position), 3)
  const geometry = new THREE.BufferGeometry()
  geometry.setAttribute('position', positions)

  const material = new THREE.RawShaderMaterial({
    vertexShader,
    fragmentShader,
    uniforms,
    side: THREE.DoubleSide,
  })

  mesh = new THREE.Mesh(geometry, material)
  scene.add(mesh)

  handleResize()
  animate()
  window.addEventListener('resize', handleResize)
})

onUnmounted(() => {
  if (animationId) cancelAnimationFrame(animationId)
  window.removeEventListener('resize', handleResize)
  if (mesh) {
    scene?.remove(mesh)
    mesh.geometry.dispose()
    if (mesh.material instanceof THREE.Material) {
      mesh.material.dispose()
    }
  }
  renderer?.dispose()
})
</script>
