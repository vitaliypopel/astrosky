from django.db import models


class Catalog(models.Model):
    name = models.CharField(max_length=100, unique=True)
    code = models.SlugField(max_length=20, unique=True)

    description = models.TextField(blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'catalogs'

    def __str__(self) -> str:
        return self.name


class Star(models.Model):
    catalog = models.ForeignKey(
        Catalog,
        on_delete=models.PROTECT,
        related_name='stars',
    )

    source_id = models.PositiveIntegerField()

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
    con = models.CharField(max_length=3, verbose_name='Constellation abbreviation')

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

    def __str__(self) -> str:
        if self.name:
            return self.name
        elif self.hip:
            return 'HIP %d' % self.hip
        elif self.hd:
            return 'HD %d' % self.hd
        elif self.hr:
            return 'HR %d' % self.hr
        elif self.gl:
            return self.gl
        elif self.bf:
            return self.bf

        return '%s %d' % (self.catalog.code.upper(), self.source_id)
