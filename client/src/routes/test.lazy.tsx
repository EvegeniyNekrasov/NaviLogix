import { createLazyFileRoute } from '@tanstack/react-router'

export const Route = createLazyFileRoute('/test')({
  component: Test,
})

function Test() {
  return <div>Hello from About!</div>
}