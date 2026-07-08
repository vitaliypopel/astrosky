export interface Observer {
  lat: number
  lon: number
}

export interface CelestialObject {
  ra: number
  dec: Number
}

export interface ObserveQuery {
  observer: Observer
  obj: CelestialObject
  dt: string | null
}

export interface ObserveManyQuery {
  observer: Observer
  objects: CelestialObject[]
  dt: string | null
}

export interface ObservationContext {
  observer: Observer
  dt: string
  jd: number
  gmst: number
  lst: number
}

export interface CelestialObjectPosition {
  obj: CelestialObject
  ha: number
  alt: number
  az: number
}

export interface Observation {
  context: ObservationContext
  positions: CelestialObjectPosition[]
}
