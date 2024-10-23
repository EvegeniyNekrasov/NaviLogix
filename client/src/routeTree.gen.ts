/* prettier-ignore-start */

/* eslint-disable */

// @ts-nocheck

// noinspection JSUnusedGlobalSymbols

// This file is auto-generated by TanStack Router

import { createFileRoute } from '@tanstack/react-router'

// Import Routes

import { Route as rootRoute } from './routes/__root'
import { Route as LoginImport } from './routes/login'

// Create Virtual Routes

const VoyagesLazyImport = createFileRoute('/voyages')()
const VesselsLazyImport = createFileRoute('/vessels')()
const TestLazyImport = createFileRoute('/test')()
const RoutesLazyImport = createFileRoute('/routes')()
const PortsLazyImport = createFileRoute('/ports')()
const CustomersLazyImport = createFileRoute('/customers')()
const IndexLazyImport = createFileRoute('/')()

// Create/Update Routes

const VoyagesLazyRoute = VoyagesLazyImport.update({
  id: '/voyages',
  path: '/voyages',
  getParentRoute: () => rootRoute,
} as any).lazy(() => import('./routes/voyages.lazy').then((d) => d.Route))

const VesselsLazyRoute = VesselsLazyImport.update({
  id: '/vessels',
  path: '/vessels',
  getParentRoute: () => rootRoute,
} as any).lazy(() => import('./routes/vessels.lazy').then((d) => d.Route))

const TestLazyRoute = TestLazyImport.update({
  id: '/test',
  path: '/test',
  getParentRoute: () => rootRoute,
} as any).lazy(() => import('./routes/test.lazy').then((d) => d.Route))

const RoutesLazyRoute = RoutesLazyImport.update({
  id: '/routes',
  path: '/routes',
  getParentRoute: () => rootRoute,
} as any).lazy(() => import('./routes/routes.lazy').then((d) => d.Route))

const PortsLazyRoute = PortsLazyImport.update({
  id: '/ports',
  path: '/ports',
  getParentRoute: () => rootRoute,
} as any).lazy(() => import('./routes/ports.lazy').then((d) => d.Route))

const CustomersLazyRoute = CustomersLazyImport.update({
  id: '/customers',
  path: '/customers',
  getParentRoute: () => rootRoute,
} as any).lazy(() => import('./routes/customers.lazy').then((d) => d.Route))

const LoginRoute = LoginImport.update({
  id: '/login',
  path: '/login',
  getParentRoute: () => rootRoute,
} as any)

const IndexLazyRoute = IndexLazyImport.update({
  id: '/',
  path: '/',
  getParentRoute: () => rootRoute,
} as any).lazy(() => import('./routes/index.lazy').then((d) => d.Route))

// Populate the FileRoutesByPath interface

declare module '@tanstack/react-router' {
  interface FileRoutesByPath {
    '/': {
      id: '/'
      path: '/'
      fullPath: '/'
      preLoaderRoute: typeof IndexLazyImport
      parentRoute: typeof rootRoute
    }
    '/login': {
      id: '/login'
      path: '/login'
      fullPath: '/login'
      preLoaderRoute: typeof LoginImport
      parentRoute: typeof rootRoute
    }
    '/customers': {
      id: '/customers'
      path: '/customers'
      fullPath: '/customers'
      preLoaderRoute: typeof CustomersLazyImport
      parentRoute: typeof rootRoute
    }
    '/ports': {
      id: '/ports'
      path: '/ports'
      fullPath: '/ports'
      preLoaderRoute: typeof PortsLazyImport
      parentRoute: typeof rootRoute
    }
    '/routes': {
      id: '/routes'
      path: '/routes'
      fullPath: '/routes'
      preLoaderRoute: typeof RoutesLazyImport
      parentRoute: typeof rootRoute
    }
    '/test': {
      id: '/test'
      path: '/test'
      fullPath: '/test'
      preLoaderRoute: typeof TestLazyImport
      parentRoute: typeof rootRoute
    }
    '/vessels': {
      id: '/vessels'
      path: '/vessels'
      fullPath: '/vessels'
      preLoaderRoute: typeof VesselsLazyImport
      parentRoute: typeof rootRoute
    }
    '/voyages': {
      id: '/voyages'
      path: '/voyages'
      fullPath: '/voyages'
      preLoaderRoute: typeof VoyagesLazyImport
      parentRoute: typeof rootRoute
    }
  }
}

// Create and export the route tree

export interface FileRoutesByFullPath {
  '/': typeof IndexLazyRoute
  '/login': typeof LoginRoute
  '/customers': typeof CustomersLazyRoute
  '/ports': typeof PortsLazyRoute
  '/routes': typeof RoutesLazyRoute
  '/test': typeof TestLazyRoute
  '/vessels': typeof VesselsLazyRoute
  '/voyages': typeof VoyagesLazyRoute
}

export interface FileRoutesByTo {
  '/': typeof IndexLazyRoute
  '/login': typeof LoginRoute
  '/customers': typeof CustomersLazyRoute
  '/ports': typeof PortsLazyRoute
  '/routes': typeof RoutesLazyRoute
  '/test': typeof TestLazyRoute
  '/vessels': typeof VesselsLazyRoute
  '/voyages': typeof VoyagesLazyRoute
}

export interface FileRoutesById {
  __root__: typeof rootRoute
  '/': typeof IndexLazyRoute
  '/login': typeof LoginRoute
  '/customers': typeof CustomersLazyRoute
  '/ports': typeof PortsLazyRoute
  '/routes': typeof RoutesLazyRoute
  '/test': typeof TestLazyRoute
  '/vessels': typeof VesselsLazyRoute
  '/voyages': typeof VoyagesLazyRoute
}

export interface FileRouteTypes {
  fileRoutesByFullPath: FileRoutesByFullPath
  fullPaths:
    | '/'
    | '/login'
    | '/customers'
    | '/ports'
    | '/routes'
    | '/test'
    | '/vessels'
    | '/voyages'
  fileRoutesByTo: FileRoutesByTo
  to:
    | '/'
    | '/login'
    | '/customers'
    | '/ports'
    | '/routes'
    | '/test'
    | '/vessels'
    | '/voyages'
  id:
    | '__root__'
    | '/'
    | '/login'
    | '/customers'
    | '/ports'
    | '/routes'
    | '/test'
    | '/vessels'
    | '/voyages'
  fileRoutesById: FileRoutesById
}

export interface RootRouteChildren {
  IndexLazyRoute: typeof IndexLazyRoute
  LoginRoute: typeof LoginRoute
  CustomersLazyRoute: typeof CustomersLazyRoute
  PortsLazyRoute: typeof PortsLazyRoute
  RoutesLazyRoute: typeof RoutesLazyRoute
  TestLazyRoute: typeof TestLazyRoute
  VesselsLazyRoute: typeof VesselsLazyRoute
  VoyagesLazyRoute: typeof VoyagesLazyRoute
}

const rootRouteChildren: RootRouteChildren = {
  IndexLazyRoute: IndexLazyRoute,
  LoginRoute: LoginRoute,
  CustomersLazyRoute: CustomersLazyRoute,
  PortsLazyRoute: PortsLazyRoute,
  RoutesLazyRoute: RoutesLazyRoute,
  TestLazyRoute: TestLazyRoute,
  VesselsLazyRoute: VesselsLazyRoute,
  VoyagesLazyRoute: VoyagesLazyRoute,
}

export const routeTree = rootRoute
  ._addFileChildren(rootRouteChildren)
  ._addFileTypes<FileRouteTypes>()

/* prettier-ignore-end */

/* ROUTE_MANIFEST_START
{
  "routes": {
    "__root__": {
      "filePath": "__root.tsx",
      "children": [
        "/",
        "/login",
        "/customers",
        "/ports",
        "/routes",
        "/test",
        "/vessels",
        "/voyages"
      ]
    },
    "/": {
      "filePath": "index.lazy.tsx"
    },
    "/login": {
      "filePath": "login.tsx"
    },
    "/customers": {
      "filePath": "customers.lazy.tsx"
    },
    "/ports": {
      "filePath": "ports.lazy.tsx"
    },
    "/routes": {
      "filePath": "routes.lazy.tsx"
    },
    "/test": {
      "filePath": "test.lazy.tsx"
    },
    "/vessels": {
      "filePath": "vessels.lazy.tsx"
    },
    "/voyages": {
      "filePath": "voyages.lazy.tsx"
    }
  }
}
ROUTE_MANIFEST_END */
