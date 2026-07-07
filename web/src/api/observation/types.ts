export interface Observer {
  lat: number
  lon: number
}

export interface StellarObject {
  ra: number
  dec: Number
}

export interface ObserveQuery {
  observer: Observer
  obj: StellarObject
  dt: string | null
}

export interface ObserveManyQuery {
  observer: Observer
  objects: StellarObject[]
  dt: string | null
}

export interface ObservationContext {
  observer: Observer
  dt: string
  jd: number
  gmst: number
  lst: number
}

export interface StellarPosition {
  obj: StellarObject
  ha: number
  alt: number
  az: number
}

export interface Observation {
  context: ObservationContext
  positions: StellarPosition[]
}
