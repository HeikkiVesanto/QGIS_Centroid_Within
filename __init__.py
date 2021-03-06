# -*- coding: utf-8 -*-
"""
/***************************************************************************
 SelectWithin
                                 A QGIS plugin
 Select centroid within and point of surface within
                             -------------------
        begin                : 2015-08-19
        copyright            : (C) 2015 by Heikki Vesanto
        email                : heikki.vesanto@gmail.com
        git sha              : $Format:%H$
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 This script initializes the plugin, making it known to QGIS.
"""


# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    """Load SelectWithin class from file SelectWithin.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .select_within import SelectWithin
    return SelectWithin(iface)
