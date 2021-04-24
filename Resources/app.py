{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [],
   "source": [
    "from flask import Flask\n",
    "\n",
    "from flask import Flask, jsonify\n",
    "import numpy as np\n",
    "import pandas as pd\n",
    "# Python SQL toolkit and Object Relational Mapper\n",
    "import sqlalchemy\n",
    "from sqlalchemy.ext.automap import automap_base\n",
    "from sqlalchemy.orm import Session\n",
    "from sqlalchemy import create_engine, func"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "metadata": {},
   "outputs": [],
   "source": [
    "engine = create_engine(\"sqlite:///hawaii.sqlite\")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "metadata": {},
   "outputs": [],
   "source": [
    "Base = automap_base()\n",
    "Base.prepare(engine, reflect=True)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "metadata": {},
   "outputs": [],
   "source": [
    "Measurement = Base.classes.measurement\n",
    "Station = Base.classes.station"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "metadata": {},
   "outputs": [],
   "source": [
    "session = Session(engine)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "metadata": {},
   "outputs": [],
   "source": [
    "app = Flask(__name__)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "metadata": {},
   "outputs": [],
   "source": [
    "@app.route('/')\n",
    "def welcome():\n",
    "    return(\n",
    "        f\"Welcome to the Hawaii Climate Analysis API!<br/>\"\n",
    "        f\"Available Routes:<br/>\"\n",
    "        f\"/api/v1.0/precipitation<br/>\"\n",
    "        f\"/api/v1.0/stations<br/>\"\n",
    "        f\"/api/v1.0/tobs<br/>\"\n",
    "        f\"/api/v1.0/temp/start/end\"\n",
    "    )"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "metadata": {},
   "outputs": [],
   "source": [
    "@app.route(\"/api/v1.0/precipitation\")\n",
    "\n",
    "def precipitation():\n",
    "   prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)\n",
    "   precipitation = session.query(Measurement.date, Measurement.prcp).\\\n",
    "    filter(Measurement.date >= prev_year).all()\n",
    "   precip = {date: prcp for date, prcp in precipitation}\n",
    "   return jsonify(precip)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "metadata": {},
   "outputs": [],
   "source": [
    "@app.route(\"/api/v1.0/stations\")\n",
    "\n",
    "def stations():\n",
    "    results = session.query(Station.station).all()\n",
    "    stations = list(np.ravel(results))\n",
    "    return jsonify(stations=stations)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "metadata": {},
   "outputs": [],
   "source": [
    "@app.route(\"/api/v1.0/tobs\")\n",
    "\n",
    "def temp_monthly():\n",
    "    prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)\n",
    "    results = session.query(Measurement.tobs).\\\n",
    "      filter(Measurement.station == 'USC00519281').\\\n",
    "      filter(Measurement.date >= prev_year).all()\n",
    "    temps = list(np.ravel(results))\n",
    "    return jsonify(temps=temps)   "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "metadata": {},
   "outputs": [],
   "source": [
    "@app.route(\"/api/v1.0/temp/<start>\")\n",
    "@app.route(\"/api/v1.0/temp/<start>/<end>\")\n",
    "\n",
    "def stats(start=None, end=None):\n",
    "    sel = [func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)]\n",
    "\n",
    "    if not end:\n",
    "        results = session.query(*sel).\\\n",
    "            filter(Measurement.date >= start).\\\n",
    "            filter(Measurement.date <= end).all()\n",
    "        temps = list(np.ravel(results))\n",
    "        return jsonify(temps)\n",
    "\n",
    "    results = session.query(*sel).\\\n",
    "        filter(Measurement.date >= start).\\\n",
    "        filter(Measurement.date <= end).all()\n",
    "    temps = list(np.ravel(results))\n",
    "    return jsonify(temps=temps)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "name": "python383jvsc74a57bd08fac594bfae6525c0c41b4041d2d72effa188cc8ead05f81b1fab2bb098927fb",
   "display_name": "Python 3.8.3 64-bit (conda)"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}