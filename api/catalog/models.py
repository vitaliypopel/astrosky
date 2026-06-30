from django.db import models


class Catalog(models.Model):
    name = models.CharField(max_length=100, unique=True)
    code = models.SlugField(max_length=20, unique=True, verbose_name='Catalog code')

    description = models.TextField(blank=True)

    class Meta:
        db_table = 'catalogs'

    def __str__(self) -> str:
        return self.name


class Constellation(models.Model):
    name = models.CharField(max_length=50, unique=True)
    code = models.CharField(max_length=3, unique=True, verbose_name='IAU code')

    ra = models.FloatField(verbose_name='Right Ascension')
    dec = models.FloatField(verbose_name='Declination')

    area = models.FloatField(verbose_name='Area in square degrees')
    area_pct = models.FloatField(verbose_name='Area in percentage')

    season = models.CharField(max_length=50, verbose_name='Observation season')

    eq = models.CharField(max_length=50, verbose_name='Equatorial zone')
    ecl = models.CharField(max_length=50, verbose_name='Ecliptic zone')
    mw = models.CharField(max_length=50, blank=True, verbose_name='Milky Way zone')

    quad = models.CharField(max_length=50, verbose_name='Quadrant')

    origin = models.CharField(max_length=20, verbose_name='Name origin')

    class Meta:
        db_table = 'constellations'

    def __str__(self) -> str:
        return self.name


class Star(models.Model):
    catalog = models.ForeignKey(
        Catalog,
        on_delete=models.PROTECT,
        related_name='stars',
    )

    source_id = models.PositiveIntegerField()

    constellation = models.ForeignKey(
        Constellation,
        on_delete=models.PROTECT,
        related_name='stars',
        null=True,
        blank=True,
    )

    hip = models.PositiveIntegerField(
        null=True,
        blank=True,
        unique=True,
        verbose_name='Hipparcos catalog ID',
    )
    hd = models.PositiveIntegerField(
        null=True,
        blank=True,
        unique=True,
        verbose_name='Henry Draper catalog ID',
    )
    hr = models.PositiveIntegerField(
        null=True,
        blank=True,
        unique=True,
        verbose_name='Harvard Revised catalog ID',
    )
    gl = models.CharField(
        max_length=20,
        blank=True,
        verbose_name='Gliese catalog ID',
    )
    bf = models.CharField(
        max_length=20,
        blank=True,
        verbose_name='Bayer/Flamsteed catalog ID',
    )

    name = models.CharField(max_length=255, blank=True)

    bayer = models.CharField(
        max_length=20,
        blank=True,
        verbose_name='Bayer designation',
    )
    flam = models.PositiveIntegerField(
        null=True,
        blank=True,
        verbose_name='Flamsteed number',
    )

    ra = models.FloatField(verbose_name='Right Ascension')
    dec = models.FloatField(verbose_name='Declination')

    dist = models.FloatField(null=True, blank=True, verbose_name='Distance in parsecs')

    mag = models.FloatField(verbose_name='Apparent visual magnitude')
    absmag = models.FloatField(
        null=True, blank=True, verbose_name='Absolute visual magnitude'
    )

    spect = models.CharField(max_length=20, blank=True, verbose_name='Spectral type')
    ci = models.FloatField(null=True, blank=True, verbose_name='Color index')

    pmra = models.FloatField(
        null=True,
        blank=True,
        verbose_name='Right Ascension proper motion',
    )
    pmdec = models.FloatField(
        null=True,
        blank=True,
        verbose_name='Declination proper motion',
    )

    rv = models.FloatField(
        null=True,
        blank=True,
        verbose_name='Radial Velocity in km/sec',
    )

    lum = models.FloatField(null=True, blank=True, verbose_name='Luminosity')

    class Meta:
        db_table = 'stars'

        constraints = [
            models.UniqueConstraint(
                fields=['catalog', 'source_id'],
                name='unique_catalog_object',
            ),
        ]

    def get_names(self) -> list[str]:
        names = []

        if self.name:
            names.append(self.name)
        if self.hip:
            names.append('HIP %d' % self.hip)
        if self.hd:
            names.append('HD %d' % self.hd)
        if self.hr:
            names.append('HR %d' % self.hr)
        if self.gl:
            names.append(self.gl)
        if self.bf:
            names.append(self.bf)

        return names

    def __str__(self) -> str:
        if names := self.get_names():
            return names[0]

        return 'Unknown'
